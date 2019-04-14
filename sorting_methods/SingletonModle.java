public class HungrySingleton {
	private static HungrySingleton instance = new HungrySingleton();
	private HungrySingleton() {}

	public static HungrySingleton getInstance() {
		return instance;
	}
}


public class LazySingleton {
	private static LazySingleton instance = null;
	private LazySingleton() {}

	public static LazySingleton getInstance() {
		if (instance == null)
			instance = new LazySingleton();
		return instance;
	}
}

public class LazySynSingleton {
	private static LazySynSingleton instance = null;
	private LazySynSingleton(){}
	public static synchronized LazySynSingleton getInstance(){
		if(instance == null)
			instance = new LazySynSingleton();
		return instance;
	}
} //缺点：粒度太大，退化到了串行化执行

public class DCL {
	//必须加上volatile关键字，不然容易引发指令重排，导致未初始化的错误
	private static volatile instance = null;
	private DCL(){}
	public static DCL getInstance(){
		if(instance == null)
			synchronized(DCL.class) {
				// double check
				if (instance == null)
					instance = new DCL();
			}
		return instance;
	}
}

public class HolderSingleton {
	private HolderSingleton(){}
	//内部类会被延迟加载
	private static class Holder {
		private static HolderSingleton instance = new HolderDemo();
	}
	public static HolderSingleton getInstance() {
		return Holder.instance;
	}
}


public class EnumSingleton {
	private EnumSingleton() {}

	//内部类会被延迟加载
	private enum EnumSingletonHolder {
		INSTANCE;
		private EnumSingleton instance;
		EnumSingletonHolder() {
			instance = new EnumSingleton();
		}
		public EnumSingleton getInstance(){
			return instance;
		}
	}
	public EnumSingleton getInstance(){
		return EnumSingletonHolder.INSTANCE.getInstance();
	}
}

public class EnumSingleton {
	private EnumSingleton() {}
	//lazy
	private enum EnumHolder {
		INSTANCE;
		private EnumSingleton instance;
		EnumHolder() {
			instance = new EnumSingleton();
		}
		public EnumSingleton getInstance(){
			return instance;
		}
	}
	public static EnumSingleton getInstance(){
		return EnumHolder.INSTANCE.getInstance();
	}
}

public class EnumSingleton {
	private EnumSingleton(){}

	private enum EnumHolder {
		INSTANCE;
		private EnumSingleton instance;
		EnumHolder() {
			instance = new EnumSingleton();
		}
		public EnumSingleton getInstance(){
			return instance;
		}
	}
	public static EnumSingleton getInstance() {
		return EnumHolder.INSTANCE.getInstance();
	}
}









