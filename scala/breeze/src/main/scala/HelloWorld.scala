import breeze.linalg.DenseVector
import breeze.linalg.DenseMatrix


object HelloWorld {
    def main(args: Array[String]) {
      val x = DenseVector(1,2,3,4)
      println(x + 1)

      val d = (x :> 2).mapValues(bool2int)
      println(d)
      println(x :* d)

      println(x(0 to 2))

      val m = DenseMatrix((1,2,3,4),(5,6,7,8))
      println(m)

      // rows
      println(m(0,::))
      println(m(1,::))

      // columns
      println(m(::,0))
      println(m(::,1))
      println(m(::,2))
      println(m(::,3))
    }

    // Something that maybe needed in our examples
    // I couldn't find a nice way apart from doing this
    def bool2int(b:Boolean) = if (b) 1 else 0
}
