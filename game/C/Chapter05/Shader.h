// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#pragma once
#include <GL/glew.h>
#include <string>
#include "Math.h"

class Shader {
public:
	Shader();
	~Shader();

	bool Load(const std::string& vertName, const std::string& fragName);
	void Unload();
	void SetActive();

private:
	bool CompileShader(const std::string& fileName, GLenum shaderType, GLuint& outShader);
	bool IsCompiler(GLuint shader);
	bool IsValidProgram();
	GLuint mVertexShader;
	GLuint mFragShader;
	GLuint mShaderProgram;
};