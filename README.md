# Drone Init
Batch initialize [drone](https://github.com/drone/drone) projects

## Features
* Setup CLI access to your drone server
* Add your secrets to a batch of drone projects

## Installation
```sh
sudo curl -L -o /bin/drone-init https://raw.githubusercontent.com/jamrizzi/drone-init/master/drone-init.py
sudo chmod +x /bin/drone-init
```

## Usage
```sh
drone-init
```

Make sure projects are properly signed so they can access the secrets.
You can read more about this [HERE](http://readme.drone.io/cli/drone-sign/).
