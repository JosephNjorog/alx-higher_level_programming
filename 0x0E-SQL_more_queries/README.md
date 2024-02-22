![bc2575fee3303b731031](https://github.com/JosephNjorog/alx-higher_level_programming/assets/141281465/0f4d0932-ed93-4aa9-aa90-359ce1d44a0a)

**For this Project, i took the following steps to achieve the solutions above. follow keenly**

**Task 0: My privileges!**

Connect to MySQL server using the provided credentials.
Write a script to list privileges of users user_0d_1 and user_0d_2.
Execute the script using mysql command passing the hostname, username, and password.
Verify the output.

**Task 1: Root user**

Connect to MySQL server using the provided credentials.
Write a script to create the MySQL user user_0d_1 with all privileges and set the password.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the creation and privileges of the user.

**Task 2: Read user**

Connect to MySQL server using the provided credentials.
Write a script to create the database hbtn_0d_2 and the user user_0d_2 with only SELECT privilege on that database.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the creation and privileges of the user.
For each subsequent task, follow a similar approach of connecting to the MySQL server, writing a script to perform the required action, executing the script using mysql command, and verifying the results.

**Task 3: Show databases**

Connect to MySQL server using the provided credentials.
Write a script to show all databases available.
Execute the script using mysql command passing the hostname, username, and password.
Verify the output to ensure it lists all databases.

**Task 4: Select privilege**

Connect to MySQL server using the provided credentials.
Write a script to grant SELECT privilege on all databases to user user_0d_2.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the privileges of user_0d_2 to ensure it has SELECT privilege on all databases.

**Task 5: Federated user**

Connect to MySQL server using the provided credentials.
Write a script to create a federated user user_federated with the same privileges as user_0d_2.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the creation and privileges of the federated user.

**Task 6: Trigger update**

Connect to MySQL server using the provided credentials.
Write a script to create a trigger that updates a column in a table when a new row is inserted.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the trigger is created successfully.

**Task 7: Schema for privileges**

Connect to MySQL server using the provided credentials.
Write a script to create a schema named hbtn_0d_tvshows and grant all privileges on it to user_0d_2.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the creation of the schema and the privileges granted.

**Task 8: Trigger on multiple tables**

Connect to MySQL server using the provided credentials.
Write a script to create a trigger that updates a column in multiple tables when a new row is inserted.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify the trigger is created successfully.

**Task 9: Events**

Connect to MySQL server using the provided credentials.
Write a script to create an event that runs daily, deleting records older than 30 days from a specified table.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify that the event is created and scheduled to run daily.

**Task 10: Stored procedures**

Connect to MySQL server using the provided credentials.
Write a script to create a stored procedure that inserts a new record into a specified table.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify that the stored procedure is created successfully.

**Task 11: Replication**

Connect to the MySQL master server using the provided credentials.
Write a script to configure the master server for replication.
Connect to the MySQL slave server using the provided credentials.
Write a script to configure the slave server to replicate from the master.
Execute both scripts using mysql command passing the hostname, username, and password.
Optionally, verify that replication is set up and working correctly.

**Task 12: Backup**

Connect to MySQL server using the provided credentials.
Write a script to perform a full backup of all databases.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify that the backup is created successfully and stored in the specified location.

**Task 13: Restore**

Connect to MySQL server using the provided credentials.
Write a script to restore a database from a previously created backup.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify that the database is restored successfully and all data is intact.

**Task 14: Security**

Connect to MySQL server using the provided credentials.
Review the current security settings and user privileges.
Write a script to update the password for an existing user or create a new user with appropriate privileges.
Execute the script using mysql command passing the hostname, username, and password.
Optionally, verify that the password has been updated or the new user has been created successfully.

**Task 15: Monitoring**

Connect to MySQL server using the provided credentials.
Install and configure monitoring tools such as Prometheus and Grafana.
Set up monitoring dashboards to track key metrics like query performance, server resources, and replication status.
Monitor the system regularly for any anomalies or performance issues.
Optionally, set up alerts to notify administrators in case of critical issues.

**Task 16: Optimization**

Connect to MySQL server using the provided credentials.
Analyze slow queries using tools like the MySQL Slow Query Log or performance schema.
Identify bottlenecks in the database schema, indexing strategy, or query patterns.
Optimize queries by adding appropriate indexes, rewriting queries, or partitioning large tables.
Monitor the performance after optimization to ensure improvements are achieved.

**Task 17: High Availability**

Set up a MySQL cluster with at least one master and multiple replicas.
Configure load balancing to distribute read and write queries across the cluster.
Implement automatic failover mechanisms to ensure uninterrupted service in case of node failures.
Test failover scenarios to verify the system's resilience to failures.
Monitor the cluster for health and performance continuously.

**Task 18: Disaster Recovery**

Set up regular backups of the MySQL databases using tools like mysqldump or Percona XtraBackup.
Store backups securely in offsite locations or cloud storage services.
Create a disaster recovery plan outlining the steps to restore data in case of catastrophic events.
Periodically test the disaster recovery plan to ensure its effectiveness.
Document the recovery procedures and train staff members on their roles during a disaster recovery operation.


