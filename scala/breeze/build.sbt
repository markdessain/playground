libraryDependencies  ++= Seq(
  "org.scalanlp" %% "breeze" % "0.12",
)

resolvers ++= Seq(
  "Sonatype Releases" at "https://oss.sonatype.org/content/repositories/releases/"
)

// or 2.11.8
scalaVersion := "2.10.4"
