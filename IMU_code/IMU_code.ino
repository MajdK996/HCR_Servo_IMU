# include <Wire.h>
# include <ICM20948_WE.h>
# define ICM20948_ADDR 0x69
ICM20948_WE myIMU = ICM20948_WE(ICM20948_ADDR);
double arr[4] = {0};
void setup () {
Wire.begin();
Serial.begin(512000);
myIMU.init();
myIMU.setAccOffsets( -16330.0 , 16450.0 , -16600.0 , 16180.0 , -16520.0 , 16690.0);
myIMU.setGyrOffsets( -115.0 , 130.0 , 105.0);
delay (1000);
myIMU.autoOffsets();
myIMU.enableAcc( true );
myIMU.enableGyr( true );
myIMU.setAccRange( ICM20948_ACC_RANGE_4G );
myIMU.setAccDLPF( ICM20948_DLPF_6 );
myIMU.setAccSampleRateDivider(7);
myIMU.setGyrRange( ICM20948_GYRO_RANGE_250 );
myIMU.setGyrDLPF( ICM20948_DLPF_6 );
myIMU.setGyrSampleRateDivider(10);
myIMU.setMagOpMode( AK09916_CONT_MODE_20HZ );
}

void loop () {
myIMU.readSensor ();
xyzFloat gValue = myIMU.getGValues();
xyzFloat gyr = myIMU.getGyrValues();
// returns magnetic flux ensity [ microT ]
xyzFloat magValue = myIMU.getMagValues();
float resultantG = myIMU.getResultantG( gValue );
// For g - values the corrected raws are used
//arr[0] = resultantG;
//arr[1] = gValue.x;
//arr[2] = gValue.y;
//arr[3] = gValue.z;
Serial.print(resultantG);
Serial.print(",");
Serial.print(gValue.x);
Serial.print(",");
Serial.print(gValue.y);
Serial.print(",");
Serial.println(gValue.z);

delay(200);
}
