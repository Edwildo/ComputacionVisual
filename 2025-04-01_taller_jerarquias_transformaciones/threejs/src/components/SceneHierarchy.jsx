import React, { useRef } from "react"
import { useFrame } from "@react-three/fiber"
import { useControls } from "leva"

export default function SceneHierarchy() {
    const groupRef = useRef()

    // Sliders de leva para rotación y posición
    const { rotationY, positionX } = useControls({
        rotationY: { value: 0, min: -Math.PI, max: Math.PI, step: 0.01 },
        positionX: { value: 0, min: -5, max: 5, step: 0.1 }
    })

    // Animación (opcional)
    useFrame(() => {
        if (groupRef.current) {
            groupRef.current.rotation.y = rotationY
            groupRef.current.position.x = positionX
        }
    })

    return (
        <group ref={groupRef} position={[0, 0, 0]}>

            {/* Hijo (cubo) */}
            <mesh position={[0, 0, 0]}>
                <boxGeometry args={[2, 2, 2]} />
                <meshStandardMaterial color="orange" />
            </mesh>

            <mesh position={[0, 2.4, 0]}>
                <sphereGeometry args={[0.7, 32, 32]} />
                <meshStandardMaterial color="red" />
            </mesh>

        </group>
    )
}
