pipeline {
agent any
stages {
  stage('SCM') {
    steps {
      git branch: 'main',
      url: 'https://github.com/surajchauhan-k/demo.git'
    }
  }
  stage("install requirment"){
    steps {
      sh "pip install -r requirements.txt --break-system-packages"
    }
  }
  stage('run test'){
    steps {
      sh "python -m coverage run -m pytest && coverage xml "
    }
  }
  stage('SonarQube Analysis') {
    steps {
      script{
      def scannerHome = tool 'sonarqube';
      withSonarQubeEnv() {
        sh "${scannerHome}/bin/sonar-scanner"
      }
      }

    }
  }
}
}