vec2 get_velocity(vec2 p) {
  vec2 v;
  float r=sqrt(p.x*p.x+p.y*p.y);
  v.x = -0.2 /r* p.x;
  v.y = -0.2 /r* p.y;
  return 1/v;
}
vec2 get_velocity(vec2 z){
  //this one is just uses the value of w as the velocity
  //z^2
  vec2 w;
  //magnitude
  float r=sqrt(z.x*z.x+z.y*z.y);
  w.x = z.x*z.x-z.y*z.y
  w.y = 2.0*z.x*z.y
  return w
}
vec2 inverse(vec2 z){
  vec2 w;
  //magnitude
  float r=sqrt(z.x*z.x+z.y*z.y);
  w.x = z.x/r/r;
  w.y = -z.y/r/r;
  return w;
}
vec2 get_velocity(vec2 p){
  return inverse(p)-p;
}
