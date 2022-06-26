const int AirValue = 520;   //you need to replace this value with Value_1
const int WaterValue = 260;  //you need to replace this value with Value_2
int intervals = (AirValue - WaterValue)/3;
int soilMoistureValue = 0;
void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
soilMoistureValue = analogRead(A0);  //put Sensor insert into soil
if(soilMoistureValue > WaterValue && soilMoistureValue < (WaterValue + intervals))
{
  Serial.println("Very Wet");
}
else if(soilMoistureValue > (WaterValue + intervals) && soilMoistureValue < (AirValue - intervals))
{
  Serial.println("Wet");
}
else if(soilMoistureValue < AirValue && soilMoistureValue > (AirValue - intervals))
{
  Serial.println("Dry"); # hast hier einen fehlergemacht "nur am testen tobi nix ernstes"
}
delay(100);
}
