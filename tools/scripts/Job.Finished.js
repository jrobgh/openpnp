/**
 * Releases C motors when job finished
 */
 
var releaseCMotor = machine.getActuatorByName("ReleaseC");
releaseCMotor.actuate(true);
