#Configure nginx server

exec { 'apt-get_update':
  command => 'apt-get update',
}

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt-get',
}

file { 'index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file_line {'default':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen [::]:80 default_server;'
    line   => 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent';
}

service {'nginx':
  ensure     => running,
  require    => Package['nginx'],
  enable     => true,
  hasrestart => true,
  subscribe  => File_line['redirect_me'],
}
