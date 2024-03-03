<<<<<<< HEAD
# installs the package puppet-lint
=======
>>>>>>> a59ccf96dc49e03ce5ea0d6d89669fa0fb9216d7
#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
