# helix-service-template
Cookiecutter template for creating a new Helix service

# Usage
1. Create a new github repo
2. Sync the github repo to your local machine.
3. `cd` into the folder
4. Install cookiecutter: `pip3 install -U cookiecutter`
5. Run cookiecutter:`cookiecutter -f https://github.com/icanbwell/helix-service-template.git -o ../`
6. This will ask you for the parameters.  Be sure to use your github repo name as the directory name
7. After generation is complete, run `make devsetup` to set up your environment.
8. In PyCharm, create a new docker compose interpreter and choose 'dev' as the service
9. Set pytest as the default test runner in PyCharm
10. Run `make tests` to check that the simple test passes.
11. Run `make up` to run your new service


# Automated builds in Github (Continuous Integration)
You will automatically have automated build and test run when you create a PR in github

# Automated deployment to AWS ECR (Continuous Deployment)
When you create a release, the docker image will be automatically pushed to AWS ECR.

NOTE: You have to create the image repo one time in AWS ECR




