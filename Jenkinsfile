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
      stage('reports') {
        allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'target/allure-results']]
        ])
        }
        }
}
