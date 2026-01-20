create DATABASE series;

create user series@'localhost' IDENTIFIED by 'series'

create user series@'%' IDENTIFIED by 'series'

grant all PRIVILEGES on series.* to series@'localhost'

grant all PRIVILEGES on series.* to series@'%'