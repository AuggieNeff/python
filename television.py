class Television:
    # Class variables omitted for brevity

    def __init__(self) -> None:
        """Initialize the Television with default values."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Turn the TV on or off."""
        self._status = not self._status

    def mute(self) -> None:
        """Mute or unmute the TV if it's on."""
        if self._status:
            self._muted = not self._muted

    # Other methods omitted for brevity
