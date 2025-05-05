import React from "react"
import { Canvas } from "@react-three/fiber"
import { OrbitControls } from "@react-three/drei"
import SceneHierarchy from "./components/SceneHierarchy"

export default function App() {
  return (
    <Canvas camera={{ position: [2, 2, 4], fov: 50 }}>
      <color attach="background" args={["white"]} />
      <ambientLight intensity={1.2} />
      <directionalLight position={[3, 5, 2]} intensity={1.5} />
      <SceneHierarchy />
      <OrbitControls />
    </Canvas>
  )
}
