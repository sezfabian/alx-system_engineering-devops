# create a file in /tmp.
file { 'school':
  path    => '/tmp/school',
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
