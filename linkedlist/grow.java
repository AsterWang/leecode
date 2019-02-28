private void grow(int minCapacity) {
	int oldCapacity = elementData.length;
	int newCapacity = oldCapacity + (oldCapacity >> 1);
	if (newCapacity - minCapacity < 0) {
		newCapacity = minCapacity;
	}
	if (newCapacity - MAX_ARRAY_SIZE > 0) {
		newCapacity = hugeCapacity(minCapacity);
	}
}