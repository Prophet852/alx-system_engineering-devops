<<<<<<< HEAD
# installs the package puppet-lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
=======
#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
>>>>>>> c307f6def84179856605542a3f9aa85b05f81af4
}
