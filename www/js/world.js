var World = function() {


}

var Ground = function() {
    this.vertices;
    this.mesh;
    this.init = function(v) {
        this.vertices = v;
        this.material = new THREE.MeshLambertMaterial({
            color: Colors.dirt
        });
        this.geometry = new THREE.PlaneGeometry(v[0].length, v.length, v[0].length, v.length);

        for (var i = 0; i < this.geometry.vertices.length; i++) {
            this.geometry.vertices[i].x = v[i];
        }
    }
}
