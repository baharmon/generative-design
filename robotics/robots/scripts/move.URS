def Program():
  DefaultGHToolTcp = p[0, 0, 0, 0, 0, 1.5708]
  DefaultGHToolWeight = 0
  DefaultGHToolCog = [0, 0, 0]
  Speed000 = 0.03
  Speed001 = 0.025
  Zone000 = 0.02
  Zone001 = 0.002
  set_tcp(DefaultGHToolTcp)
  set_payload(DefaultGHToolWeight, DefaultGHToolCog)
  movej([0, -1.5708, -1.5708, -1.5708, 1.5708, 0], a=3.1416, v= 0.314, r=Zone000)
  movej(p[1, 0, 0.4, 0, 3.14159, 0],a=3.14159,v= 0.032,r=Zone001)
end