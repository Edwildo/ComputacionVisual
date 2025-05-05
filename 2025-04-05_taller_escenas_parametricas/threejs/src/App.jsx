import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { ParametricScene } from './components/ParametricScene'

function App() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <Canvas camera={{ position: [5, 5, 5], fov: 60 }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[5, 5, 5]} />
        <ParametricScene />
        <OrbitControls />
      </Canvas>
    </div>
  )
}

export default App
