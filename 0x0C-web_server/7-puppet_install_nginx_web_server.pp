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

file { '404.html':
  ensure  => 'present',
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page',
}

file {'default':
    ensure  => 'present',
    content => 'listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm index.nginx-debian.html;
    rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;    
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }',
    path    => '/etc/nginx/sites-available/default',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
