from docker import Client
from io import BytesIO


class DockerPlugin(object):
    
    dockerfile = '''
    FROM dockerfile/ubuntu
    # Install Java.
    RUN \
        echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
        add-apt-repository -y ppa:webupd8team/java && \
        apt-get update && \
        apt-get install -y oracle-java8-installer && \
        rm -rf /var/lib/apt/lists/* && \
        rm -rf /var/cache/oracle-jdk8-installer

    # Define commonly used JAVA_HOME variable
    ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

    ENV JETTY_VERSION 9.2.5.v20141112
    RUN wget http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-distribution-${JETTY_VERSION}.zip -O /tmp/jetty.zip

    # Unpack
    RUN cd /opt && jar xf /tmp/jetty.zip
    RUN ln -s /opt/jetty-distribution-${JETTY_VERSION} /opt/jetty
    RUN rm /tmp/jetty.zip

    ENV JETTY_HOME /opt/jetty
    ENV PATH $PATH:$JETTY_HOME/bin
    ADD http://tomcat.apache.org/tomcat-6.0-doc/appdev/sample/sample.war /opt/jetty/webapps/
    WORKDIR /opt/jetty
    CMD java -jar start.jar
    EXPOSE 8080
    #CMD ["/opt/start-jetty.sh"]
    '''
    
    def buildDockerfile(self):
        encDockerfile = BytesIO(self.dockerfile.encode('utf-8'))
        cli = Client(base_url='tcp://192.168.1.20:2375')
        response = [line for line in cli.build(fileobj=encDockerfile, rm=True, tag='webpy' )]
        print response
        
        
if __name__ == '__main__':
    d = DockerPlugin()
    d.buildDockerfile()