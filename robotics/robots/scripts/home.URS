def Program():
  DefaultGHToolTcp = p[0, 0, 0, 0, 0, 1.5708]
  DefaultGHToolWeight = 0
  DefaultGHToolCog = [0, 0, 0]
  Speed000 = 0.03
  Zone000 = 0.02
  set_tcp(DefaultGHToolTcp)
  set_payload(DefaultGHToolWeight, DefaultGHToolCog)
  movej([0, -1.5708, -1.5708, -1.5708, 1.5708, 0], a=3.1416, v= 0.314, r=Zone000)
end