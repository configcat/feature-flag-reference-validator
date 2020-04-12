# Steps to deploy
## Preparation
1. Execute the script on the test file.
   ```bash
   python configcat-validator.py PKDVCLf-Hq-h-kCzMp-L7Q/NB1-IBFV50erQbSn7DXGIw ./sample_to_scan -v
   ```
2. Increase the version in `setup.py`.
3. Commit & Push

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

  Create a new [Github release](https://github.com/configcat/feature-flag-reference-validator/releases) with a new version tag and release notes.

At this point you should have a new [docker image](https://cloud.docker.com/u/configcat/repository/docker/configcat/feature-flag-reference-validator) and [pypi package](https://pypi.org/project/configcat-flag-reference-validator/) with the new version you set earlier.

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
   circleci orb publish orb.yml configcat/feature-flag-reference-validator@[MAJOR].[MINOR].[PATCH]
   ```
   > Example: `circleci orb publish integrations/circleci/orb.yml configcat/feature-flag-reference-validator@1.2.1`
   
   > You can also publish non-public developer versions with the `dev:` version prefix like: `feature-flag-reference-validator@dev:1.2.1`
6. Make sure the new version is available in the [Orb Registry](https://circleci.com/orbs/registry/orb/configcat/feature-flag-reference-validator).