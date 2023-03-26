#FROM openjdk:8-jre-slim
FROM amazoncorretto:8-alpine
EXPOSE 8080 5005
RUN mkdir -p /opt/target
COPY target/aws-proserve-java-greeting.war /opt/target/
WORKDIR /opt/target
ENV _JAVA_OPTIONS '-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005'

CMD ["java", "-jar", "aws-proserve-java-greeting.war"]
