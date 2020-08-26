pipeline {
    agent any
    environment {
        email = 'deathikun@gmail.com'
        password = '918273645q'
        username = 'Death-kun'
    }
    stages {
      stage('Build') {
        steps {
          bat "pip install -r requirements.txt"
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