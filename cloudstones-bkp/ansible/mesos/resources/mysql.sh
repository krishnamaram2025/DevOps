password=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $11}')
mysqladmin --user=root --password="$password" password aaBB@@cc1122
