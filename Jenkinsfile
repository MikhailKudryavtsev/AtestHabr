pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
          bat "pip install -r requirements.txt"
          }
          }
      stage('Test') {
        steps {
            bat "set email=deathikun@gmail.com"
            bat "set password=918273645q"
            bat "set username=Death-kun"
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
