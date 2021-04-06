#  Install and configure Nginx web server

package { 'nginx':
  ensure => 'present',
  name   => 'nginx',
}

file { 'index.html':
  ensure  => 'present',
  path    => '/etc/nginx/html/index.html',
  content => 'Holberton School\n',
}

file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen [::]:80 default_server;',
  line   => 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service {'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['default'],
}
