void setup() {
fullScreen();
strokeWeight(10);
stroke(100, 100);
}
void draw() {
if (mousePressed) line(pmouseX, pmouseY, mouseX, mouseY);
}
