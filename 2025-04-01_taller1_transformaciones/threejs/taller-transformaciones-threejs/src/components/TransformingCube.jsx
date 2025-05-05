// src/components/TransformingCube.jsx
import React from "react";
import { useRef } from "react";
import { useFrame } from "@react-three/fiber";

export default function TransformingCube() {
  const ref = useRef();

  useFrame(({ clock }) => {
    const t = clock.getElapsedTime();

    ref.current.position.x = 2 * Math.cos(t);
    ref.current.position.y = 2 * Math.sin(t);
    ref.current.rotation.x += 0.01;
    ref.current.rotation.y += 0.01;

    const scale = 1 + 0.3 * Math.sin(t);
    ref.current.scale.set(scale, scale, scale);
  });

  return (
    <mesh ref={ref}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="tomato" />
    </mesh>
  );
}
