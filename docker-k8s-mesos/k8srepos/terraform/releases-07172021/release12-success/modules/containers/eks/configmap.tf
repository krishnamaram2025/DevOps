data "aws_caller_identity" "current" {}

locals {
  auth_worker_roles = [
    for index in range(0, var.create_eks ? local.worker_group_count : 0) : {
      worker_role_arn = "arn:${data.aws_partition.current.partition}:iam::${data.aws_caller_identity.current.account_id}:role/${element(
        coalescelist(
          aws_iam_instance_profile.workers.*.role,
          data.aws_iam_instance_profile.custom_worker_group_iam_instance_profile.*.role_name,
          [""]
        ),
        index,
      )}"
      platform = lookup(
        var.worker_groups[index],
        "platform",
        local.workers_group_defaults["platform"]
      )
    }
  ]

  # Convert to format needed by aws-auth ConfigMap
  configmap_roles = [
    for role in 
      local.auth_worker_roles:
    {
      rolearn  = replace(role["worker_role_arn"], replace(var.iam_path, "/^//", ""), "")
      username = role["platform"] == "fargate" ? "system:node:{{SessionName}}" : "system:node:{{EC2PrivateDNSName}}"
      groups = tolist(concat(
        [
          "system:bootstrappers",
          "system:nodes",
        ],
        role["platform"] == "windows" ? ["eks:kube-proxy-windows"] : [],
        role["platform"] == "fargate" ? ["system:node-proxier"] : [],
      ))
    }
  ]
}

resource "kubernetes_config_map" "aws_auth" {
  count      = var.create_eks && var.manage_aws_auth ? 1 : 0
  depends_on = [null_resource.wait_for_cluster]

  metadata {
    name      = "aws-auth"
    namespace = "kube-system"
    labels = merge(
      {
        "app.kubernetes.io/managed-by" = "Terraform"
        "terraform.io/module" = "terraform-aws-modules.eks.aws"
      },
      var.aws_auth_additional_labels
    )
  }

  data = {
    mapRoles = yamlencode(
      distinct(concat(
        local.configmap_roles,
        var.map_roles,
      ))
    )
    mapUsers    = yamlencode(var.map_users)
    mapAccounts = yamlencode(var.map_accounts)
  }
}

