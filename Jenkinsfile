node {
    agent {
        docker { image 'python:3.10.12-slim'}
    }
  stage('SCM') {
    git branch: 'main',
    url: 'https://github.com/surajchauhan-k/demo.git'
  }
  stage("install requirment"){
    sh "pip install -r requirements.txt"
  }
  stage('run test'){
    sh "coverage run -m pytest && coverage xml "
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarqube';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner \
      -Dsonar.sources=. "
    }
  }
}