# Drone Init
Batch initialize [drone](https://github.com/drone/drone) projects

## Features
* Setup CLI access to your drone server
* Add your secrets to a batch of drone projects

## Usage
```
curl -LO https://raw.githubusercontent.com/jamrizzi/drone-init/master/drone-init.py
python drone-init.py
```
Make sure projects are properly signed so they can access the secrets.
You can read more about this [HERE](http://readme.drone.io/cli/drone-sign/).
