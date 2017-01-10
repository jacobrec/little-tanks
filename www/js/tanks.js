var Tank = function(w) {
    this.world = w;

    this.position = new Vector3();
    this.velocity = new Vector3();
    this.bodyAngle = 0;
    this.headAngle = 0;
    this.turretAngle = 0;

    this.update = function(delta) {
        this.velocity.addScaledVector(this.position, delta);
    }
    this.shoot = function() {

    }
    this.setPosition(pos) {
        this.position.copy(pos);
    }
}
