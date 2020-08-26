pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
          bat "pip install -r rearequirements.txt"
          }
          }
      stage('Test') {
        steps {
          bat "pytest -v --alluredir=target/allure-results"
          }
          }
      stage ('Results') {
          steps {
              allure jdk: '', results: [[path: "target/allure-results"]]
          }
    }
}
}
