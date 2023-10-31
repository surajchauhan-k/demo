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
      sh "python -m pytest --cov --cov-report=xml --junitxml=xunit-reports/xunit-result.xml "
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