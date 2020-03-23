Gazebo_bot:
1) Mybot.xacro: It contains the bot specific urdf code for a skid steered bot
2) Mybot.gazebo: It contains the plugins used in the bot simulation on gazebo
3)Launch File 
4)Gazebo world for the simulation

Scripts:
 1) GPS Client : When called gives the latitude from Subscriber based on GPS Garmin 18x
 2) GPS Service : Sends Latitude values when called
 3) Subscriber for Latitude values
 4) Publisher for Latitude values
 5) Autonomous Traversal of a bot simulated in gazebo using IMU values and GPS
