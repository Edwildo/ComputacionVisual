import { useMemo } from 'react'

const data = [
  { x: 0, y: 0, z: 0, type: 'box', scale: 1, color: 'orange' },
  { x: 2, y: 0, z: 0, type: 'sphere', scale: 1.2, color: 'skyblue' },
  { x: 4, y: 0, z: 0, type: 'box', scale: 1.4, color: 'green' },
  { x: 0, y: 2, z: 0, type: 'sphere', scale: 1, color: 'purple' },
  { x: 2, y: 2, z: 0, type: 'box', scale: 0.9, color: 'red' },
]

export function ParametricScene() {
  const meshes = useMemo(() =>
    data.map((item, i) => {
      const position = [item.x, item.y, item.z]
      const scale = item.scale
      const color = item.color
      const isSphere = item.type === 'sphere'

      return (
        <mesh key={i} position={position} scale={scale}>
          {isSphere
            ? <sphereGeometry args={[0.5, 32, 32]} />
            : <boxGeometry args={[1, 1, 1]} />}
          <meshStandardMaterial color={color} />
        </mesh>
      )
    }), []
  )

  return <>{meshes}</>
}
