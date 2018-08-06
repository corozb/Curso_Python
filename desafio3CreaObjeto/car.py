class Car:
    _CARS = ['''
                       \
          __________ ___/_>________
         /  ____ \ <>     |  ____  \
        =\_/ __ \_\_______|_/ __ \__D
    ________(__)_____________(__)____
    ''',
    '''
           -           __
      --          ~( @\  \
     ---   _________]_[__/_>________
         /  ____ \ <>     |  ____  \
        =\_/ __ \_\_______|_/ __ \__D
    ________(__)_____________(__)____
    ''',
    '''
        o_______________}o{
        |              |   \
        |    911       |____\_____
        | _____        |    |_o__ |
        [/ ___ \       |   / ___ \|
       []_/.-.\_\______|__/_/.-.\_[]
          |(O)|             |(O)|
           '-'   ScS         '-'
    ---   ---   ---   ---   ---   ---
    ''']

    def __init__(self, _is_running_off):
        self._is_running_off = _is_running_off

    def running_off(self):
        self._is_running_off = True
        self._display_image()

    def running_on(self):
        self._is_running_on = False
        self._display_image()

    def max_speed(self):
        self._is_max_speed = False
        self._display_image()

    def _display_image(self):
        if self._is_running_off:
            print(self._CARS[0])

        elif self._is_running_on:
            print(self._CARS[1])

        else:
            print(self._CARS[2])
