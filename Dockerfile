# Use Maven to build the app
FROM maven:3.9.6-eclipse-temurin-17 AS builder

WORKDIR /app

# Copy pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source code and build
COPY src ./src
RUN mvn clean package -DskipTests

# Use a slim OpenJDK image to run the app
FROM eclipse-temurin:17-jre

WORKDIR /app

# Copy only the final fat jar
COPY --from=builder /app/target/servers-1.0-SNAPSHOT.jar app.jar

# Run the app
ENTRYPOINT ["java", "-jar", "app.jar"]
