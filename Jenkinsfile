pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
          sh "pip install -r rearequirements.txt"
          }
          }
      stage('Test') {
        steps {
          sh "pytest -v --alluredir=target/allure-results"
          }
          }
      stage ('Results') {
        allure jdk: '', results: [[path: "target/allure-results"]]
    }
}
}
