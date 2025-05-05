import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { useState } from 'react'
import { ModelViewer } from './components/ModelViewer'

function App() {
  const [format, setFormat] = useState('obj')

  const getModelPath = () => {
    if (format === 'obj') return '/handtruck.obj'
    if (format === 'stl') return '/teamugstl.stl'
    return '/scene.gltf'
  }
  


  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <select
        style={{ position: 'absolute', top: 20, left: 20, zIndex: 10 }}
        value={format}
        onChange={(e) => setFormat(e.target.value)}
      >
        <option value="obj">OBJ</option>
        <option value="stl">STL</option>
        <option value="gltf">GLTF</option>
      </select>

      <Canvas camera={{ position: [0, 0, 5] }}>
        <ambientLight intensity={0.8} />
        <directionalLight position={[5, 5, 5]} />
        <ModelViewer format={format} path={getModelPath()} />
        <OrbitControls />
      </Canvas>
    </div>
  )
}

export default App
