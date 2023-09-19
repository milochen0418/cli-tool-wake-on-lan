# java-wake-on-lan
Wake on Lan  (WoL) in java code 

## Usage 
### get info of jre and jdk
- check JRE version

$ java -version
```
java version "1.8.0_381"
Java(TM) SE Runtime Environment (build 1.8.0_381-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.381-b09, mixed mode)```
```

- check JDK version

$ javac -version
```
javac 17.0.8
```

### compile
$ javac WakeOnLan.java 

But we can compile by the following way to make sure the version of JRE is the same as to the JDK. 
$ javac -source 1.8 -target 1.8 WakeOnLan.java

### execute 
$ java WakeOnLan 111.112.255.255 54:EA:F9:70:43:B3

