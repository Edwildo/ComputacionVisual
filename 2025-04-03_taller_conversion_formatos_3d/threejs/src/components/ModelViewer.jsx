import { useLoader } from '@react-three/fiber'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'
import { useMemo } from 'react'

export const ModelViewer = ({ format, path }) => {
  const model = useMemo(() => {
    if (format === 'obj') return useLoader(OBJLoader, path)
    if (format === 'stl') return useLoader(STLLoader, path)
    return useLoader(GLTFLoader, path) // ahora maneja "gltf"
  }, [format, path])

  if (!model) return null

  if (format === 'gltf') {
    return <primitive object={model.scene} />
  }

  if (format === 'stl') {
    return (
      <mesh>
        <primitive object={model} attach="geometry" />
        <meshStandardMaterial color="orange" />
      </mesh>
    )
  }

  return <primitive object={model} />
}
