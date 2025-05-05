// sketch_transformaciones.pde
float angle = 0;

void setup() {
  size(600, 600, P3D);
  frameRate(60);
}

void draw() {
  background(0);
  lights();
  translate(width/2, height/2, 0);

  // Traslación ondulante
  float offsetX = 100 * sin(frameCount * 0.05);
  float offsetY = 100 * cos(frameCount * 0.05);
  translate(offsetX, offsetY);

  // Rotación continua
  rotateX(angle);
  rotateY(angle * 0.5);

  // Escalado cíclico
  float scaleFactor = 1 + 0.5 * sin(frameCount * 0.05);
  scale(scaleFactor);

  // Cubo
  fill(255, 100, 100);
  stroke(255);
  box(100);

  angle += 0.02;

  // Para exportar frames (descomenta si quieres capturarlos)
  saveFrame("frames/frame_####.png");
}