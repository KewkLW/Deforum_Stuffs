import gradio as gr
import os

def generate_text(main_text, additional_text, prefix, suffix, output_dir):
    main_text = [mt for mt in main_text.split('\n') if mt.strip() != ''] if main_text else ['']
    additional_text = [at for at in additional_text.split('\n') if at.strip() != ''] if additional_text else ['']
    prefix = [p for p in prefix.split('\n') if p.strip() != ''] if prefix else ['']
    suffix = [s for s in suffix.split('\n') if s.strip() != ''] if suffix else ['']

    output_file_path = os.path.join(output_dir, 'output.txt')
    with open(output_file_path, 'w') as f:
        for mt in main_text:
            for at in additional_text:
                for p in prefix:
                    for s in suffix:
                        line = ' '.join(filter(None, [p, mt, at, s]))
                        if line.strip():
                            f.write(line + '\n')
                    f.write('\n')

    return f"Text file has been written successfully to {output_file_path}."

iface = gr.Interface(fn=generate_text, 
                     inputs=[gr.components.Textbox(lines=2, label="Main Text"),
                             gr.components.Textbox(lines=2, label="Additional Text"),
                             gr.components.Textbox(lines=2, label="Prefix"),
                             gr.components.Textbox(lines=2, label="Suffix"),
                             gr.components.Textbox(lines=1, label="Output Directory")], 
                     outputs=gr.components.Textbox())

iface.launch()
