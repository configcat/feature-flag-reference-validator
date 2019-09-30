# Steps to deploy
## Preparation
1. Execute the script on the test file.
   ```bash
   configcat-validator 92jVCNQBzuYAenfTn0PZQw/grLLS9QKeEiFJPNLan8K4w ./sample_to_scan -s=testcdn.configcat.com -v
   ```
2. Increase the versions in `setup.py`.

## Publish a new docker image and pypi package
Use the **same version** for the git tag as in the 2. step of the Preparation section.
- Via git tag
    1. Create a new version tag.
       ```bash
       git tag [MAJOR].[MINOR].[PATCH]
       ```
       > Example: `git tag 1.2.1`
    2. Push the tag.
       ```bash
       git push origin --tags
       ```
- Via Github release 

  Create a new [Github release](https://github.com/configcat/flag-reference-validator/releases) with a new version tag and release notes.

At this point you should have a new [docker image](https://cloud.docker.com/u/configcat/repository/docker/configcat/flag-reference-validator) and [pypi package](https://pypi.org/project/configcat-flag-reference-validator/) with the new version you set earlier.

## Publish a new CircleCI orb
1. Install the [CircleCI CLI](https://circleci.com/docs/2.0/local-cli/#quick-installation).
2. Follow [these instructions](https://circleci.com/docs/2.0/local-cli/#configuring-the-cli) to configure the CLI.
3. Update the new pypi package and docker image versions in `integrations/circleci/orb.yml`.
4. Validate the orb configuration.
   ```bash
   circleci orb validate integrations/circleci/orb.yml
   ```
5. Publish the new orb.
   ```bash
   circleci orb publish orb.yml configcat/flag_reference_validator@[MAJOR].[MINOR].[PATCH]
   ```
   > Example: `circleci orb publish orb.yml configcat/flag_reference_validator@1.2.1`
   
   > You can also publish non-public developer versions with the `dev:` version prefix like: `flag_reference_validator@dev:1.2.1`
6. Make sure the new version is available in the [Orb Registry](https://circleci.com/orbs/registry/orb/configcat/flag_reference_validator).