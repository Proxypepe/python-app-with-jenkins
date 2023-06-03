def imageName = 'proxypepe/demo'
def registry = 'localhost:5000'

def commitID() {
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    commitID
}

node('master'){
  stage('Checkout') {
    git branch: 'main',
      url: ''
  }
    // stage('Unit Tests'){
  //   def imageTest = docker.build("${imageName}-test", 
  //   "-f Dockerfile.test .")
  //   imageTest.inside{
  //     sh 'python test_main.py'
  //   }
  //   // sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
  //   // junit "$PWD/reports/*.xml"
  // }
  def imageTest = docker.build("${imageName}-test", "-f Dockerfile.test .")
  stage('Pre-integration Tests'){
    parallel(
      'Quality Tests': {
          sh "docker run --rm ${imageName}-test pylint ."
      },
       'Unit Tests': {
          sh "docker run --rm ${imageName}-test pytest"
        },
      'Security Tests': {
        sh "docker run --rm ${imageName}-test safety check -r main.py"
      }
    )
  }

  stage('Build') {
    docker.build("${imageName}", "-f Dockerfile .")
  }

  stage('Push') {
    docker.withRegistry(registry, 'registry') {
      docker.image(imageName).push(commitID())

      if (env.BRANCH_NAME == 'develop') {
          docker.image(imageName).push('develop')
      }
    }
  }
}
